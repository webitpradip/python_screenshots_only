@echo off

REM Check if the virtual environment exists
if not exist "env\Scripts\activate" (
    echo Creating virtual environment...
    python -m venv env
) else (
    echo Virtual environment already exists.
)

REM Activate the virtual environment
call env\Scripts\activate

REM Install the required packages
echo Installing required packages...
pip install -r requirements.txt

REM Run the app
echo Running the application...
python app.py

echo Running
pause
