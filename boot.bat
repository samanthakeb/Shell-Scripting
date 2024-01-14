@echo off
set /p answer=Would you like to play Rock Paper Scissors? (yes/no): 
if /i "%answer%"=="yes" (
   start "Game File" "C:\Users\saman\OneDrive\Documents\rock_paper_scissors.py"
) else (
    echo That's too bad, maybe next time.
)
pause