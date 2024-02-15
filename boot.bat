@echo off
set /p answer=Would you like to play Rock Paper Scissors? (yes/no): 
if /i "%answer%"=="yes" (
   python rock_paper_scissors.py
) else (
    echo That's too bad, maybe next time.
)
pause