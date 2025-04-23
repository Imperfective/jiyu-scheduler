
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
  exec('start /min cmd /c "cd backend && streamlit run app.py"', (err, stdout, stderr) => {
    if (err) {
      console.error('Python backend 실행 오류:', err);
      return;
    }
  });

  setTimeout(() => {
    createWindow();
  }, 5000);
});
