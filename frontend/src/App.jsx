import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import Layout from './components/Layout';
import Home from './pages/Home';
import QuestionBank from './pages/QuestionBank';
import ExamLobby from './pages/ExamLobby';
import ExamActive from './pages/ExamActive';
import ExamResult from './pages/ExamResult';
import ReviewCenter from './pages/ReviewCenter';
import LiteratureHub from './pages/LiteratureHub';
import Statistics from './pages/Statistics';

export function App() {
  return (
    <ThemeProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="questions" element={<QuestionBank />} />
            <Route path="exam" element={<ExamLobby />} />
            <Route path="exam/active" element={<ExamActive />} />
            <Route path="exam/result" element={<ExamResult />} />
            <Route path="review" element={<ReviewCenter />} />
            <Route path="literature" element={<LiteratureHub />} />
            <Route path="statistics" element={<Statistics />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;
