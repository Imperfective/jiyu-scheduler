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
  // 빌드 시 asarUnpack으로 포함된 위치에 맞춰 경로 수정
  const exePath = path.join(process.resourcesPath, 'public', 'app_backend.exe');

  exec(`start "" "${exePath}"`, (err, stdout, stderr) => {
    if (err) {
      console.error('❌ app_backend.exe 실행 오류:', err);
      return;
    }
  });

  // Streamlit 서버가 실행되기를 기다린 후 창 열기
  setTimeout(() => {
    createWindow();
  }, 5000);
});
