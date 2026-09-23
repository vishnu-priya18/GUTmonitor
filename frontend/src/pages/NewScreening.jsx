import React, { useState, useEffect } from 'react';
import { Layers, Play, RefreshCw, CheckCircle2, Sparkles, FileText, Image as ImageIcon } from 'lucide-react';
import ImageUploader from '../components/ImageUploader';
import DisclaimerBanner from '../components/DisclaimerBanner';
import PipelineVisualizer from '../components/PipelineVisualizer';
import RiskGauge from '../components/RiskGauge';
import { api } from '../api/client';

export default function NewScreening({ setActivePage, setScreeningResult }) {
  const [mode, setMode] = useState('demo'); // 'demo' or 'live'
  const [demoSamples, setDemoSamples] = useState([]);
  const [selectedCaseId, setSelectedCaseId] = useState('');
  
  // Live input state
  const [tongueFile, setTongueFile] = useState(null);
  const [tonguePreview, setTonguePreview] = useState(null);
  const [skinFile, setSkinFile] = useState(null);
  const [skinPreview, setSkinPreview] = useState(null);

  // Questionnaire form state matching clinical model features exactly!
  const [formData, setFormData] = useState({
    age: 35,
    bmi: 24.5,
    abdominal_pain_severity: 1,
    bloating_frequency: 1,
    acid_reflux_frequency: 1,
    constipation_score: 0,
    diarrhea_score: 0,
    nausea_vomiting: 0,
    dietary_fiber_intake: 'medium',
    fatty_food_intake: 'medium',
    alcohol_consumption: 'none',
    smoking_status: 'non-smoker',
    physical_activity_hours: 4.0,
    perceived_stress_level: 4,
    sleep_duration_hrs: 7.0
  });

  const [loading, setLoading] = useState(false);
  const [evalResult, setEvalResult] = useState(null);

  useEffect(() => {
    // Load demo preset cases
    api.getDemoSamples()
      .then(samples => {
        setDemoSamples(samples);
        if (samples.length > 0) {
          setSelectedCaseId(samples[0].id);
        }
      })
      .catch(err => console.error("Could not load demo samples", err));
  }, []);

  const handleTongueSelected = (file) => {
    setTongueFile(file);
    if (file) {
      setTonguePreview(URL.createObjectURL(file));
    } else {
      setTonguePreview(null);
    }
  };

  const handleSkinSelected = (file) => {
    setSkinFile(file);
    if (file) {
      setSkinPreview(URL.createObjectURL(file));
    } else {
      setSkinPreview(null);
    }
  };

  const handleRunScreening = async () => {
    setLoading(true);
    setEvalResult(null);

    try {
      let res;
      if (mode === 'demo' && selectedCaseId) {
        res = await api.evaluateDemoCase(selectedCaseId);
      } else {
        res = await api.predictMultimodal(tongueFile, skinFile, formData);
      }
      setEvalResult(res);
      setScreeningResult(res);
    } catch (err) {
      alert("Screening failed: " + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-8">
      <DisclaimerBanner />

      <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-slate-800 pb-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center gap-2">
            <Layers className="w-5 h-5 text-teal-400" />
            <span>New Multimodal GI Screening</span>
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">Select Expo Demo Preset Mode or enter live patient images and clinical symptoms</p>
        </div>

        {/* Mode Selector Toggle */}
        <div className="bg-slate-850 p-1 rounded-lg border border-slate-700 flex items-center gap-1">
          <button
            type="button"
            onClick={() => setMode('demo')}
            className={`px-3 py-1.5 rounded-md text-xs font-semibold transition-all ${
              mode === 'demo' ? 'bg-teal-500 text-slate-950 shadow' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Project Expo Demo Mode
          </button>
          <button
            type="button"
            onClick={() => setMode('live')}
            className={`px-3 py-1.5 rounded-md text-xs font-semibold transition-all ${
              mode === 'live' ? 'bg-teal-500 text-slate-950 shadow' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Live Input Upload
          </button>
        </div>
      </div>

      {/* Mode A: Expo Demo Mode Preset Case Selection */}
      {mode === 'demo' && (
        <div className="bg-slate-850 border border-teal-500/40 rounded-xl p-6 shadow-xl space-y-4">
          <div className="flex items-center space-x-2 text-teal-300 font-semibold text-xs uppercase tracking-wider">
            <Sparkles className="w-4 h-4 text-teal-400" />
            <span>Select Pre-Loaded Research Dataset Profile</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            {demoSamples.map((c) => (
              <div
                key={c.id}
                onClick={() => setSelectedCaseId(c.id)}
                className={`p-4 rounded-xl border cursor-pointer transition-all ${
                  selectedCaseId === c.id
                    ? 'bg-teal-500/10 border-teal-400 text-white shadow-lg'
                    : 'bg-slate-900 border-slate-800 text-slate-300 hover:border-slate-700'
                }`}
              >
                <div className="flex items-center justify-between mb-2">
                  <span className="text-xs font-bold">{c.name}</span>
                  {selectedCaseId === c.id && <CheckCircle2 className="w-4 h-4 text-teal-400" />}
                </div>
                <div className="text-[11px] text-slate-400 font-mono mt-1">Expected: {c.expected_risk}</div>
                <div className="flex items-center space-x-2 mt-3 text-[10px] text-slate-400">
                  <span className="bg-slate-800 px-2 py-0.5 rounded border border-slate-700">Tongue Image</span>
                  <span className="bg-slate-800 px-2 py-0.5 rounded border border-slate-700">Skin Image</span>
                  <span className="bg-slate-800 px-2 py-0.5 rounded border border-slate-700">15 Symptoms</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Mode B: Live Input Forms */}
      {mode === 'live' && (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          
          {/* Image Uploaders */}
          <div className="space-y-6 bg-slate-850 p-6 rounded-xl border border-slate-700/60">
            <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-700 pb-3">
              <ImageIcon className="w-4 h-4 text-teal-400" />
              <span>Visual Modalities Upload</span>
            </h3>

            <ImageUploader
              label="Modality 1: Tongue Image Upload"
              sublabel="TMC / Tongue Surface mucosal image"
              onImageSelected={handleTongueSelected}
              currentPreview={tonguePreview}
            />

            <ImageUploader
              label="Modality 2: Skin Image Upload (Complementary)"
              sublabel="ISIC / Cutaneous visual sign image"
              onImageSelected={handleSkinSelected}
              currentPreview={skinPreview}
            />
          </div>

          {/* Questionnaire Form */}
          <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4">
            <h3 className="text-sm font-bold text-white flex items-center gap-2 border-b border-slate-700 pb-3">
              <FileText className="w-4 h-4 text-purple-400" />
              <span>Modality 3: Symptoms & Lifestyle Questionnaire</span>
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
                  {[0,1,2,3,4].map(v => <option key={v} value={v}>{v} - {v===0?'Never':v===1?'Rare':v===2?'Weekly':'Daily/Severe'}</option>)}
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
                <label className="text-slate-300 font-medium">Perceived Stress (1-10)</label>
                <input 
                  type="number" 
                  min="1" max="10"
                  value={formData.perceived_stress_level}
                  onChange={(e) => setFormData({...formData, perceived_stress_level: parseInt(e.target.value) || 5})}
                  className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
                />
              </div>

              <div>
                <label className="text-slate-300 font-medium">Sleep (Hours/night)</label>
                <input 
                  type="number" 
                  step="0.5"
                  value={formData.sleep_duration_hrs}
                  onChange={(e) => setFormData({...formData, sleep_duration_hrs: parseFloat(e.target.value) || 7.0})}
                  className="w-full mt-1 bg-slate-900 border border-slate-700 rounded px-2.5 py-1.5 text-white"
                />
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Action Button */}
      <div className="flex justify-center pt-4">
        <button
          type="button"
          onClick={handleRunScreening}
          disabled={loading}
          className="bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-600 hover:to-emerald-700 text-slate-950 font-extrabold text-sm px-8 py-3.5 rounded-xl shadow-xl shadow-teal-500/20 transition-all flex items-center space-x-3 disabled:opacity-50"
        >
          {loading ? (
            <>
              <RefreshCw className="w-5 h-5 animate-spin" />
              <span>Executing PyTorch & Multimodal Fusion Pipeline...</span>
            </>
          ) : (
            <>
              <Play className="w-5 h-5 fill-slate-950" />
              <span>RUN MULTIMODAL SCREENING PIPELINE</span>
            </>
          )}
        </button>
      </div>

      {/* Result Output Display */}
      {evalResult && (
        <div className="space-y-6 pt-6 border-t border-slate-800">
          <PipelineVisualizer
            tongueResult={evalResult.tongue}
            skinResult={evalResult.skin}
            clinicalResult={evalResult.clinical}
            fusionResult={evalResult.fusion}
          />

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <div className="lg:col-span-1">
              <RiskGauge
                riskLevel={evalResult.fusion?.preliminary_risk_indication}
                confidence={evalResult.fusion?.confidence}
                probabilities={evalResult.fusion?.risk_probabilities}
              />
            </div>

            <div className="lg:col-span-2 bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4">
              <h4 className="text-sm font-bold text-white uppercase tracking-wider border-b border-slate-700 pb-2">
                Modality Specific Backend Outputs
              </h4>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs">
                <div className="bg-slate-900 p-3.5 rounded-lg border border-slate-800">
                  <span className="text-teal-400 font-bold block mb-1">Tongue Model Output</span>
                  <p className="text-slate-300 font-semibold">{evalResult.tongue?.predicted_class}</p>
                  <p className="text-slate-400 text-[11px] mt-1">Confidence: {(evalResult.tongue?.confidence * 100).toFixed(1)}%</p>
                </div>

                <div className="bg-slate-900 p-3.5 rounded-lg border border-slate-800">
                  <span className="text-emerald-400 font-bold block mb-1">Skin Model Output</span>
                  <p className="text-slate-300 font-semibold">{evalResult.skin?.predicted_class}</p>
                  <p className="text-slate-400 text-[11px] mt-1">Confidence: {(evalResult.skin?.confidence * 100).toFixed(1)}%</p>
                </div>

                <div className="bg-slate-900 p-3.5 rounded-lg border border-slate-800">
                  <span className="text-purple-400 font-bold block mb-1">Clinical Model Output</span>
                  <p className="text-slate-300 font-semibold">{evalResult.clinical?.predicted_risk}</p>
                  <p className="text-slate-400 text-[11px] mt-1">Confidence: {(evalResult.clinical?.confidence * 100).toFixed(1)}%</p>
                </div>
              </div>

              <div className="pt-2">
                <button
                  onClick={() => setActivePage('results')}
                  className="text-xs text-teal-400 hover:text-teal-300 font-semibold flex items-center space-x-1"
                >
                  <span>View Detailed Screening Results & Explainability →</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
