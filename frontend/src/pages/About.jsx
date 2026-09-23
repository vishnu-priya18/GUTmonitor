import React from 'react';
import { Info, Award, HeartHandshake, ShieldCheck } from 'lucide-react';
import DisclaimerBanner from '../components/DisclaimerBanner';

export default function About() {
  return (
    <div className="space-y-6 max-w-4xl">
      <DisclaimerBanner />

      <div className="border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <Info className="w-5 h-5 text-teal-400" />
          <span>About GI-Vision AI</span>
        </h2>
        <p className="text-xs text-slate-400 mt-0.5">Biomedical Engineering Project Expo 2026 Submission</p>
      </div>

      <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4 text-xs text-slate-300 leading-relaxed">
        <h3 className="text-sm font-bold text-teal-300 uppercase tracking-wider">Project Claim & Contribution</h3>
        <p className="bg-slate-900 p-4 rounded-lg border border-teal-500/30 text-slate-200 font-medium italic">
          "A multimodal AI framework that explores the combination of tongue-image features, complementary skin-image features, and structured gastrointestinal symptom/lifestyle information for preliminary GI health screening."
        </p>

        <h3 className="text-sm font-bold text-white pt-3 uppercase tracking-wider">Expo Demonstration Features</h3>
        <ul className="list-disc pl-5 space-y-1.5 text-slate-400">
          <li><strong>Offline Expo Mode:</strong> Pre-loaded research dataset cases for seamless presentation without internet access.</li>
          <li><strong>Live PyTorch Backend:</strong> Real trained neural weights (`.pt`) and joblib pipelines executed dynamically via FastAPI.</li>
          <li><strong>Medical Safety Safeguards:</strong> Transparent risk indication categories (Low, Moderate, Higher Risk) with explicit disclaimers.</li>
        </ul>
      </div>
    </div>
  );
}
