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
  win.loadURL('http://localhost:8501'); // Streamlit 기본 포트
}

app.whenReady().then(() => {
  // Streamlit이 아닌 app_backend.exe 실행
  exec('start /min "" "backend\\app_backend.exe"', (err, stdout, stderr) => {
    if (err) {
      console.error('app_backend.exe 실행 오류:', err);
      return;
    }
  });

  // Streamlit 서버가 완전히 뜨는 시간 고려
  setTimeout(() => {
    createWindow();
  }, 5000);  // 필요 시 더 늘려도 됨
});
