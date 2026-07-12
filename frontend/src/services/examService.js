import api from './api';

export const examService = {
  getQuestions: async (params = {}) => {
    const response = await api.get('/questions/', { params });
    return response.data;
  },

  getTopics: async () => {
    const response = await api.get('/questions/topics');
    return response.data;
  },

  getQuestionById: async (id) => {
    const response = await api.get(`/questions/${id}`);
    return response.data;
  },

  getQuestionsBatch: async (ids) => {
    const response = await api.post('/questions/batch', { ids });
    return response.data;
  },

  submitExam: async (answers, timeSpent) => {
    const response = await api.post('/questions/submit', {
      answers,
      time_spent: timeSpent,
    });
    return response.data;
  },
};

export default examService;
