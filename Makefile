WIN = windows
LIN = linux
SCRIPT = seawar.py
WIN_EXE = --onefile $(SCRIPT) --distpath $(WIN) --workpath $(WIN) --specpath $(WIN) --clean
LIN_EXE = --onefile $(SCRIPT) --distpath $(LIN) --workpath $(LIN) --specpath $(LIN) --clean


windows:
	mkdir $(WIN)
	pip install pyinstaller
	pyinstaller $(WIN_EXE)
	./$(WIN)/seawar.exe

linux:
	mkdir $(LIN)
	pip3 install pyinstaller
	pyinstaller $(LIN_EXE)
	./$(LIN)/seawar.exe

web:
	open http://127.0.0.1:5500/seawar.html

clean:
	rm -rf $(WIN)
	rm -rf $(LIN)