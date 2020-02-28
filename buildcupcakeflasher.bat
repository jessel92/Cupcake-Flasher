echo Packaging CupCake Flasher
cd venv/Scripts & activate.bat & cd .. & cd .. & pyinstaller --onefile --icon=img/cf_icon.ico main.py & del main.spec & rd /s /q "build" & cd dist & MOVE main.exe ../main.exe & cd .. & rd dist & echo Packaging complete & rename main.exe "Cupcake Flasher.exe" & PAUSE
