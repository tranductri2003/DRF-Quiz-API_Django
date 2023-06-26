import { Route, Routes } from 'react-router-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import QuizSelect from './components/QuizSelect';
import RandomQuiz from './components/RandomQuiz';
import React from 'react';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<QuizSelect />} />
        <Route path="/r/:topic" element={<RandomQuiz />} />
      </Routes>
    </Router>
  );
}

export default App;