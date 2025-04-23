# jiyu-scheduler
# 📦 지유 근무 스케줄러 (Windows 자동 빌드용)

이 프로젝트는 `Electron + Python (Streamlit)` 기반의 데스크탑 근무 스케줄 생성기입니다.  
`GitHub Actions`를 통해 **자동으로 Windows EXE 파일을 빌드**합니다.

---

## 🚀 기능 요약

- 근무자 자동 배정 (하루 6명)
- 필수 인원 조건 / 휴무 요청 반영
- 연속 근무 조절 (기본 2일, 추가근무자는 최대 3일)
- Streamlit 기반 GUI 인터페이스
- Electron으로 감싸진 데스크탑 앱

---

## 🧪 GitHub Actions 자동 빌드 사용법

1. 이 레포지토리를 GitHub에 Push (예: `main` 브랜치)
2. GitHub Actions가 자동으로 실행됨
3. `.exe` 결과는 **Actions → Artifacts → 지유근무스케줄러_EXE.zip** 으로 제공됨

---

## 🛠️ 로컬 개발 방법 (선택)

```bash
npm install
pip install -r backend/requirements.txt
npm start
```

> 또는 `npm run dist` → `dist/` 폴더에 `.exe` 생성됨

---

## ✅ 요구사항

- Node.js 18 이상
- Python 3.9 이상

---

## 📁 주요 폴더

| 경로 | 설명 |
|------|------|
| `backend/` | Python + Streamlit 코드 |
| `.github/workflows/` | GitHub Actions 자동화 설정 |
| `main.js` | Electron 메인 실행 파일 |

---

## 👏 만든 사람

- 자동화 템플릿 제작: ChatGPT
- 개발자: 당신 🎉

---

