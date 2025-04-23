const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const path = require('path');

function createWindow () {
  const win = new BrowserWindow({
    width: 1200,
    height: 800,
    webPreferences: {
      nodeIntegration: true
    }
  });
  win.loadURL('http://localhost:8501');
}

app.whenReady().then(() => {
  const exePath = path.join(process.resourcesPath, 'backend', 'app_backend.exe');

  exec(`start "" "${exePath}"`, (err, stdout, stderr) => {
    if (err) {
      console.error('app_backend.exe 실행 오류:', err);
      return;
    }
  });

  setTimeout(() => {
    createWindow();
  }, 5000);
});
