import React, { useState } from 'react';
import { BookOpen, Send } from 'lucide-react';
import DisclaimerBanner from '../components/DisclaimerBanner';
import { api } from '../api/client';

export default function SymptomsLifestyle() {
  const [formData, setFormData] = useState({
    age: 38,
    bmi: 26.2,
    abdominal_pain_severity: 2,
    bloating_frequency: 2,
    acid_reflux_frequency: 2,
    constipation_score: 1,
    diarrhea_score: 1,
    nausea_vomiting: 0,
    dietary_fiber_intake: 'medium',
    fatty_food_intake: 'high',
    alcohol_consumption: 'moderate',
    smoking_status: 'non-smoker',
    physical_activity_hours: 3.0,
    perceived_stress_level: 6,
    sleep_duration_hrs: 6.5
  });

  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await api.predictClinical(formData);
      setResult(res);
    } catch (err) {
      alert("Submission failed: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <DisclaimerBanner />

      <div className="border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <BookOpen className="w-5 h-5 text-purple-400" />
          <span>Modality 3: GI Symptoms & Lifestyle Questionnaire</span>
        </h2>
        <p className="text-xs text-slate-400 mt-0.5">Scikit-Learn Random Forest Pipeline trained on 1,000 clinical GI records</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <form onSubmit={handleSubmit} className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4">
          <h3 className="text-sm font-bold text-white uppercase tracking-wider border-b border-slate-700 pb-2">
            Clinical Feature Inputs (Exact Model Schema)
          </h3>

          <div className="grid grid-cols-2 gap-3 text-xs">
            <div>
              <label className="text-slate-300 font-medium">Age</label>
              <input 
                type="number" 
                value={formData.age}
                onChange={(e) => setFormData({...formData, age: parseInt(e.target.value) || 30})}
                className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
              />
            </div>
            <div>
              <label className="text-slate-300 font-medium">BMI (kg/m²)</label>
              <input 
                type="number" 
                step="0.1"
                value={formData.bmi}
                onChange={(e) => setFormData({...formData, bmi: parseFloat(e.target.value) || 24.0})}
                className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
              />
            </div>

            <div>
              <label className="text-slate-300 font-medium">Abdominal Pain (0-5)</label>
              <select 
                value={formData.abdominal_pain_severity}
                onChange={(e) => setFormData({...formData, abdominal_pain_severity: parseInt(e.target.value)})}
                className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
              >
                {[0,1,2,3,4,5].map(v => <option key={v} value={v}>{v} - {v===0?'None':v<=2?'Mild':v<=4?'Moderate':'Severe'}</option>)}
              </select>
            </div>

            <div>
              <label className="text-slate-300 font-medium">Bloating (0-4)</label>
              <select 
                value={formData.bloating_frequency}
                onChange={(e) => setFormData({...formData, bloating_frequency: parseInt(e.target.value)})}
                className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
              >
                {[0,1,2,3,4].map(v => <option key={v} value={v}>{v}</option>)}
              </select>
            </div>

            <div>
              <label className="text-slate-300 font-medium">Acid Reflux (0-4)</label>
              <select 
                value={formData.acid_reflux_frequency}
                onChange={(e) => setFormData({...formData, acid_reflux_frequency: parseInt(e.target.value)})}
                className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
              >
                {[0,1,2,3,4].map(v => <option key={v} value={v}>{v}</option>)}
              </select>
            </div>

            <div>
              <label className="text-slate-300 font-medium">Dietary Fiber</label>
              <select 
                value={formData.dietary_fiber_intake}
                onChange={(e) => setFormData({...formData, dietary_fiber_intake: e.target.value})}
                className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
              >
                <option value="low">Low Fiber</option>
                <option value="medium">Medium Fiber</option>
                <option value="high">High Fiber</option>
              </select>
            </div>

            <div>
              <label className="text-slate-300 font-medium">Stress Level (1-10)</label>
              <input 
                type="number" 
                min="1" max="10"
                value={formData.perceived_stress_level}
                onChange={(e) => setFormData({...formData, perceived_stress_level: parseInt(e.target.value) || 5})}
                className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
              />
            </div>

            <div>
              <label className="text-slate-300 font-medium">Sleep Duration (hrs)</label>
              <input 
                type="number" 
                step="0.5"
                value={formData.sleep_duration_hrs}
                onChange={(e) => setFormData({...formData, sleep_duration_hrs: parseFloat(e.target.value) || 7.0})}
                className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full bg-purple-600 hover:bg-purple-700 disabled:opacity-50 text-white font-bold py-2.5 rounded-lg text-xs shadow transition-all flex items-center justify-center space-x-2"
          >
            <Send className="w-4 h-4" />
            <span>{loading ? "Evaluating Random Forest..." : "EVALUATE CLINICAL MODEL"}</span>
          </button>
        </form>

        {result && (
          <div className="bg-slate-850 p-6 rounded-xl border border-purple-500/40 space-y-4 shadow-xl">
            <h3 className="text-sm font-bold text-purple-300 uppercase tracking-wider border-b border-slate-700 pb-2">
              Clinical Model Output
            </h3>

            <div className="bg-slate-900 p-4 rounded-lg border border-slate-800">
              <span className="text-xs text-slate-400 block uppercase tracking-wider">Predicted Tabular Risk</span>
              <span className="text-xl font-bold text-white font-mono">{result.predicted_risk}</span>
              <span className="text-xs text-purple-400 font-mono block mt-1">Confidence: {(result.confidence * 100).toFixed(1)}%</span>
            </div>

            <div className="space-y-2 pt-2">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Top Contributing Clinical Factors</span>
              {(result.top_contributing_factors || []).map((factor, idx) => (
                <div key={idx} className="bg-slate-900 p-2.5 rounded border border-slate-800 text-xs flex justify-between items-center">
                  <div>
                    <span className="text-slate-200 font-medium">{factor.feature}</span>
                    <span className="text-[10px] text-slate-400 block font-mono">Value: {factor.value}</span>
                  </div>
                  <span className="text-purple-400 font-mono text-[11px] font-bold">Imp: {factor.importance}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
