import React, { useState } from 'react';
import { Activity, Upload, Sparkles } from 'lucide-react';
import ImageUploader from '../components/ImageUploader';
import DisclaimerBanner from '../components/DisclaimerBanner';
import { api } from '../api/client';

export default function TongueAnalysis() {
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
      alert("Please select or upload a tongue image first.");
      return;
    }
    setLoading(true);
    try {
      const res = await api.predictTongue(file);
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
          <Activity className="w-5 h-5 text-teal-400" />
          <span>Modality 1: Tongue Image Analysis</span>
        </h2>
        <p className="text-xs text-slate-400 mt-0.5">Standalone inference module using PyTorch MobileNetV3 for tongue mucosal features</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4">
          <ImageUploader 
            label="Upload Tongue Image" 
            sublabel="TMC / TCM Tongue Dataset Standards"
            onImageSelected={handleSelected}
            currentPreview={preview}
          />

          <button
            onClick={handleAnalyze}
            disabled={loading || !file}
            className="w-full bg-teal-500 hover:bg-teal-600 disabled:opacity-50 text-slate-950 font-bold py-2.5 rounded-lg text-xs shadow transition-all"
          >
            {loading ? "Processing with PyTorch..." : "ANALYZE TONGUE IMAGE"}
          </button>
        </div>

        {result && (
          <div className="bg-slate-850 p-6 rounded-xl border border-teal-500/40 space-y-4 shadow-xl">
            <h3 className="text-sm font-bold text-teal-300 uppercase tracking-wider border-b border-slate-700 pb-2">
              Tongue Model Output
            </h3>

            <div className="bg-slate-900 p-4 rounded-lg border border-slate-800">
              <span className="text-xs text-slate-400 block uppercase tracking-wider">Predicted Tongue Class</span>
              <span className="text-xl font-bold text-white font-mono">{result.predicted_class}</span>
              <span className="text-xs text-teal-400 font-mono block mt-1">Confidence: {(result.confidence * 100).toFixed(1)}%</span>
            </div>

            <div className="bg-amber-950/40 p-3.5 rounded-lg border border-amber-500/30 text-xs text-amber-200">
              <span className="font-bold block mb-1">CLINICAL FEATURE NOTE:</span>
              {result.clinical_note}
            </div>

            <div className="space-y-2 pt-2">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Probabilities Across Tongue Classes</span>
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
