import React, { useState } from 'react';
import { Activity, Upload } from 'lucide-react';
import ImageUploader from '../components/ImageUploader';
import DisclaimerBanner from '../components/DisclaimerBanner';
import { api } from '../api/client';

export default function SkinAnalysis() {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleSelected = (f) => {
    setFile(f);
    setPreview(f ? URL.createObjectURL(f) : null);
  };

  const handleAnalyze = async () => {
    if (!file) {
      alert("Please select or upload a skin image first.");
      return;
    }
    setLoading(true);
    try {
      const res = await api.predictSkin(file);
      setResult(res);
    } catch (err) {
      alert("Analysis failed: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6">
      <DisclaimerBanner />

      <div className="border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <Activity className="w-5 h-5 text-emerald-400" />
          <span>Modality 2: Complementary Skin Visual Information</span>
        </h2>
        <p className="text-xs text-slate-400 mt-0.5">Dermatological visual feature extractor based on ISIC dataset standards</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4">
          <ImageUploader 
            label="Upload Skin Image" 
            sublabel="ISIC Dermatology Standard"
            onImageSelected={handleSelected}
            currentPreview={preview}
          />

          <button
            onClick={handleAnalyze}
            disabled={loading || !file}
            className="w-full bg-emerald-500 hover:bg-emerald-600 disabled:opacity-50 text-slate-950 font-bold py-2.5 rounded-lg text-xs shadow transition-all"
          >
            {loading ? "Processing with PyTorch..." : "ANALYZE SKIN IMAGE"}
          </button>
        </div>

        {result && (
          <div className="bg-slate-850 p-6 rounded-xl border border-emerald-500/40 space-y-4 shadow-xl">
            <h3 className="text-sm font-bold text-emerald-300 uppercase tracking-wider border-b border-slate-700 pb-2">
              Skin Model Output
            </h3>

            <div className="bg-slate-900 p-4 rounded-lg border border-slate-800">
              <span className="text-xs text-slate-400 block uppercase tracking-wider">Predicted Skin Feature Class</span>
              <span className="text-xl font-bold text-white font-mono">{result.predicted_class}</span>
              <span className="text-xs text-emerald-400 font-mono block mt-1">Confidence: {(result.confidence * 100).toFixed(1)}%</span>
            </div>

            <div className="bg-sky-950/40 p-3.5 rounded-lg border border-sky-500/30 text-xs text-sky-200">
              <span className="font-bold block mb-1">COMPLEMENTARY VISUAL ROLE:</span>
              {result.clinical_note}
            </div>

            <div className="space-y-2 pt-2">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Skin Feature Probabilities</span>
              {Object.entries(result.class_probabilities || {}).map(([cls, prob]) => (
                <div key={cls} className="flex justify-between text-xs font-mono text-slate-300">
                  <span>{cls}</span>
                  <span>{(prob * 100).toFixed(1)}%</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
