const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const mongoose = require('mongoose');  // MongoDB 연결을 위한 mongoose 라이브러리
const app = express();
const port = 3000;

app.use(bodyParser.json());

// MongoDB 연결 설정 (데이터베이스에 연결)
mongoose.connect('mongodb://localhost:27017/running_data', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('MongoDB 연결 성공');
}).catch(err => {
  console.error('MongoDB 연결 실패', err);
});

// MongoDB 스키마 및 모델 정의
const RunningDataSchema = new mongoose.Schema({
  age: Number,
  gender: String,
  heartRate: Number,
  incline: Number,
  experience: String,
  goalDistance: Number,
  distanceCovered: Number,
  result: String
});

const RunningData = mongoose.model('RunningData', RunningDataSchema);

// Swift에서 데이터를 받는 API
app.post('/api/send-data', (req, res) => {
  const { age, gender, heartRate, incline, experience, goalDistance, distanceCovered } = req.body;

  // Python 파일 실행
  const pyScript = 'python3 ../prompt_ex.py';
  const pyArgs = `${age} ${gender} ${heartRate} ${incline} ${experience} ${goalDistance} ${distanceCovered}`;

  exec(`${pyScript} ${pyArgs}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Python 실행 오류: ${error.message}`);
      return res.status(500).json({ error: 'Python 실행 오류' });
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
      return res.status(500).json({ error: 'Python 오류' });
    }

    const result = stdout.trim();  // Python 스크립트에서 받은 결과

    // MongoDB에 저장
    const runningData = new RunningData({
      age,
      gender,
      heartRate,
      incline,
      experience,
      goalDistance,
      distanceCovered,
      result
    });

    runningData.save().then(() => {
      console.log('데이터 저장 완료');
      res.json({ result });
    }).catch(err => {
      console.error('데이터 저장 오류', err);
      res.status(500).json({ error: '데이터 저장 오류' });
    });
  });
});

app.listen(port, () => {
  console.log(`서버가 포트 ${port}에서 실행 중입니다.`);
});
