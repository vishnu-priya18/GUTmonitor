import axios from 'axios';

const API_BASE_URL = '/api';

export const api = {
  // Predict single modalities
  predictTongue: async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await axios.post(`${API_BASE_URL}/predict/tongue`, formData);
    return response.data;
  },

  predictSkin: async (file) => {
    const formData = new FormData();
    formData.append('file', file);
    const response = await axios.post(`${API_BASE_URL}/predict/skin`, formData);
    return response.data;
  },

  predictClinical: async (questionnaireData) => {
    const response = await axios.post(`${API_BASE_URL}/predict/clinical`, questionnaireData);
    return response.data;
  },

  // Multimodal End-to-End Prediction
  predictMultimodal: async (tongueFile, skinFile, questionnaireData) => {
    const formData = new FormData();
    if (tongueFile) formData.append('tongue_file', tongueFile);
    if (skinFile) formData.append('skin_file', skinFile);
    if (questionnaireData) formData.append('clinical_payload', JSON.stringify(questionnaireData));

    const response = await axios.post(`${API_BASE_URL}/predict/multimodal`, formData);
    return response.data;
  },

  // Model Performance Results
  getModalityMetrics: async (modality) => {
    const response = await axios.get(`${API_BASE_URL}/results/${modality}/metrics`);
    return response.data;
  },

  // Demo Mode
  getDemoSamples: async () => {
    const response = await axios.get(`${API_BASE_URL}/demo/samples`);
    return response.data;
  },

  evaluateDemoCase: async (caseId) => {
    const response = await axios.post(`${API_BASE_URL}/demo/evaluate_case/${caseId}`);
    return response.data;
  }
};
