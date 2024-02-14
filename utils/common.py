import glob
import inspect
import json
import logging.config
import os
import platform
import re
from datetime import datetime
from pathlib import Path
import subprocess
import pandas as pd
import requests
import sys

from utils.config import set_and_get_config_data


def get_logger():
    config_file_path = Path(__file__).parent.parent / "config/logging.conf"
    project_path = Path(__file__).parent.parent
    # Define a custom log filename
    log_filename = project_path.as_posix() + "/" + "reports/logs/logfile.log"

    # Check if the log directory exists; if not, create it
    log_directory = os.path.dirname(log_filename)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        print(f"Log File Created in {log_directory}")

    logging.config.fileConfig(config_file_path, defaults={"log_filename": log_filename})
    # logger_name = inspect.stack()[1][3]
    # Get the caller's frame
    caller_frame = inspect.currentframe().f_back

    # Extract the caller function name
    logger_name = caller_frame.f_code.co_name
    logger = logging.getLogger(logger_name)
    return logger


def get_test_data(sheet_name):
    excel_path = Path(__file__).parent.parent / "utils/testdata.xlsx"
    df = pd.read_excel(excel_path, sheet_name=sheet_name, dtype=str)
    df_filled = df.fillna("")
    return df_filled.to_dict(orient="records")


def get_html_reports():
    reports = []
    try:
        path = Path(__file__).parent.parent / f"reports/htmlreport/regression_*.html"
        report = os.path.abspath(glob.glob(f"{path}")[-1])
        reports.append(report)
    except Exception as e:
        print("Report not ready, Error", e)
    return reports


# Read current date
def read_date():
    return str(datetime.today().strftime("%Y-%m-%d"))


def read_time():
    return str(datetime.today().strftime("%I-%M-%S-%p"))


def clean_directory(directory):
    exclude_dirs = [
        "screenshots",
        "allure_report",
        "htmlreport",
        "logs",
        "xml_report",
        "failed",
        "passed",
    ]
    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            except Exception as e:
                print(f"Failed to delete file: {file_path} - {e}")

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if dir.lower() not in exclude_dirs:
                try:
                    os.rmdir(dir_path)
                    print(f"Deleted folder: {dir_path}")
                except Exception as e:
                    print(f"Failed to delete folder: {dir_path} - {e}")


def get_appium_server_version(appium_server_url):
    try:
        # Send a GET request to the Appium server's status endpoint
        response = requests.get(f"{appium_server_url}/status")
        response_json = response.json()

        # Extract and return the Appium server version
        appium_server_version = (
            response_json.get("value", {})
            .get("build", {})
            .get("version", "Version not found")
        )
        return appium_server_version

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while getting Appium server version: {str(e)}")
        return None


def check_appium(server):
    try:
        # Get the Appium version
        appium_version = get_appium_server_version(server)
        print("Running Appium version:", appium_version)

        # Check Appium version and print an error message if it's 1.22 or lower
        if appium_version and tuple(map(int, re.findall(r"\d+", appium_version))) <= (
                1,
                22,
                0,
        ):
            raise EnvironmentError(
                f"Appium version {appium_version} is installed. Please upgrade to version 2.0.0 or higher."
            )

    except ImportError:
        raise EnvironmentError("Appium is not installed or accessible.")


def find_java_jdk_path():
    # Define the search patterns for JDK installation directories on Linux, macOS, and Windows
    linux_pattern = "/usr/lib/jvm/java-*"
    mac_pattern = "/Library/Java/JavaVirtualMachines/jdk*"
    windows_pattern = r"C:\Program Files\Java\jdk-*"

    # Determine the current operating system
    current_os = os.name

    if current_os == "posix":  # Linux or macOS
        # Use glob to find JDK directories that match the patterns on Linux and macOS
        jdk_paths = glob.glob(linux_pattern) + glob.glob(mac_pattern)
    elif current_os == "nt":  # Windows
        # Use glob to find JDK directories that match the pattern on Windows
        jdk_paths = glob.glob(windows_pattern)
    else:
        raise EnvironmentError("Unsupported operating system.")

    if not jdk_paths:
        raise EnvironmentError("No Java JDK installations found matching the patterns.")

    # Return the first matching JDK path (you can modify this if multiple JDKs are installed)
    return jdk_paths[0]


def find_android_sdk_path():
    # Try to find the Android SDK path based on the user's home directory
    home = str(Path.home())
    potential_sdk_paths = [
        os.path.join(home, "AppData", "Local", "Android", "Sdk"),  # Windows
        os.path.join(home, "Library", "Android", "sdk"),  # macOS
        os.path.join(home, "Android", "Sdk"),  # Linux
    ]

    for path in potential_sdk_paths:
        if os.path.exists(path):
            return path

    # If the SDK path is not found, you can raise an exception or return None
    raise EnvironmentError(
        "Android SDK path not found. Please install the Android SDK and set it up correctly."
    )


def find_sdk_directory():
    system = platform.system()
    home_dir = os.path.expanduser("~")

    if system == "Linux":
        possible_paths = [
            "/usr/local/android-sdk",  # Common installation path on Linux
            f"{home_dir}/Android/Sdk",  # Android Studio default SDK path
            "/usr/lib/android-sdk",
        ]
    elif system == "Darwin":
        possible_paths = [
            "/usr/local/android-sdk",  # Common installation path on macOS
            f"{home_dir}/Library/Android/sdk",  # Android Studio default SDK path on macOS
        ]
    elif system == "Windows":
        possible_paths = [
            f"{home_dir}\\AppData\\Local\\Android\\Sdk",  # Default SDK path on Windows
        ]
    else:
        print("Unsupported operating system.")
        return None

    for path in possible_paths:
        if os.path.exists(path):
            return path

    return None


def check_environment():
    try:
        # Check if JAVA_HOME is set
        java_home = os.environ.get("JAVA_HOME")

        if not java_home:
            print("JAVA_HOME environment variable is not set. Setting it now...")
            try:
                java_jdk_path = find_java_jdk_path()
                if java_jdk_path is None:
                    print("JAVA Path Not Found....")
                    return
                os.environ["JAVA_HOME"] = java_jdk_path
                java_home = os.environ["JAVA_HOME"]
                print("JAVA_HOME set to:", java_home)
            except EnvironmentError as e:
                print(f"Error: {e}")

        if not java_home:
            print("JAVA_HOME is still not set. Please set it manually.")
            return

        # Check if ANDROID_HOME is set
        android_home = os.environ.get("ANDROID_HOME")

        if not android_home:
            print("ANDROID_HOME environment variable is not set. Setting it now...")
            try:
                android_sdk_path = find_sdk_directory()
                if android_sdk_path is None:
                    print("SDK Path Not Found")
                    return
                os.environ["ANDROID_HOME"] = android_sdk_path
                android_home = os.environ["ANDROID_HOME"]
                print("ANDROID_HOME set to:", android_home)
            except EnvironmentError as e:
                print(f"Error: {e}")

        if not android_home:
            print("ANDROID_HOME is still not set. Please set it manually.")
            return

        # Check Android SDK paths
        android_sdk_paths = [
            os.path.join(android_home, "platform-tools"),
            # os.path.join(android_home, "build-tools"),
            # Add more paths as needed
        ]

        for path in android_sdk_paths:
            if not os.path.exists(path):
                raise EnvironmentError(f"Android SDK path not found: {path}")

    except EnvironmentError as e:
        print(f"Error: {e}")
        sys.exit(1)


def get_android_version():
    try:
        # Run the ADB command to retrieve the Android version
        result = subprocess.run(
            ["adb", "shell", "getprop", "ro.build.version.release"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Check if the command was successful
        if result.returncode == 0:
            android_version = result.stdout.strip()
            return android_version
        else:
            # Handle the case where the ADB command failed
            error_message = result.stderr.strip()
            return f"Error: {error_message}"
    except FileNotFoundError:
        return "Error: ADB is not installed or not in the system PATH."


def create_json_capabilities():
    data = set_and_get_config_data()
    device_capabilities = {
        "platformName": "Android",
        "platformVersion": get_android_version(),  # Replace with the actual Android version
        "app": data["apkPath"],  # Replace with the actual app path
        "automationName": "UIAutomator2",
        "appPackage": data["appPackage"],  # Replace with the actual app package name
        "appActivity": data["appActivity"],  # Replace with the actual app activity name
        "autoGrantPermissions": True,  # Set to True or False based on your requirements
        "udid": data["udid"],  # Replace with the actual device UDID
        "newCommandTimeout": 300,  # Adjust the timeout value as needed
    }
    device_capabilities_json = json.dumps(device_capabilities)
    json_file_path = Path(__file__).parent.parent / "device_capabilities.json"
    with open(json_file_path, "w") as json_file:
        json.dump(device_capabilities, json_file, indent=4)
