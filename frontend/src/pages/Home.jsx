import React from 'react';
import { Activity, Layers, ShieldCheck, Database, BarChart3, ArrowRight, CheckCircle2 } from 'lucide-react';
import DisclaimerBanner from '../components/DisclaimerBanner';

export default function Home({ setActivePage }) {
  return (
    <div className="space-y-8">
      <DisclaimerBanner />

      {/* Hero Section */}
      <div className="bg-gradient-to-br from-slate-850 via-slate-900 to-slate-950 border border-slate-800 rounded-2xl p-8 lg:p-12 shadow-2xl relative overflow-hidden">
        <div className="max-w-3xl relative z-10">
          <span className="inline-flex items-center gap-1.5 text-[11px] font-mono font-semibold text-teal-400 bg-teal-500/10 border border-teal-500/30 px-3 py-1 rounded-full uppercase tracking-wider mb-4">
            <Activity className="w-3.5 h-3.5" /> BME Project Expo 2026 Research Prototype
          </span>
          
          <h1 className="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-white leading-tight">
            Multimodal AI-Based <br />
            <span className="text-transparent bg-clip-text bg-gradient-to-r from-teal-400 via-emerald-400 to-sky-400">
              Gastrointestinal Disease Screening
            </span>
          </h1>

          <p className="mt-4 text-sm sm:text-base text-slate-300 leading-relaxed">
            Integrating non-invasive <strong>Tongue Mucosal Images</strong>, <strong>Complementary Skin Visual Signs</strong>, and <strong>Structured GI Symptoms & Lifestyle Profiles</strong> using a Gated Multimodal Neural Fusion Architecture.
          </p>

          <div className="mt-8 flex flex-wrap items-center gap-4">
            <button
              onClick={() => setActivePage('new_screening')}
              className="bg-teal-500 hover:bg-teal-600 text-slate-950 font-bold px-6 py-3 rounded-xl shadow-lg shadow-teal-500/25 transition-all flex items-center space-x-2 text-sm"
            >
              <span>Launch Screening Demo</span>
              <ArrowRight className="w-4 h-4" />
            </button>
            
            <button
              onClick={() => setActivePage('performance')}
              className="bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold px-6 py-3 rounded-xl transition-all flex items-center space-x-2 text-sm"
            >
              <BarChart3 className="w-4 h-4 text-teal-400" />
              <span>View Trained Metrics</span>
            </button>
          </div>
        </div>
      </div>

      {/* 3 Modalities Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-850 border border-slate-700/60 rounded-xl p-6 shadow-lg">
          <div className="w-10 h-10 rounded-lg bg-teal-500/10 text-teal-400 flex items-center justify-center mb-4">
            <Activity className="w-5 h-5" />
          </div>
          <h3 className="text-base font-bold text-white mb-1">Modality 1: Tongue Image</h3>
          <p className="text-xs text-slate-400 leading-relaxed mb-4">
            Analyzes mucosal color, coating density, and surface characteristics reflecting microflora and circulatory changes.
          </p>
          <span className="text-[10px] font-mono text-teal-400 bg-teal-500/10 px-2.5 py-1 rounded border border-teal-500/20 block w-max">
            PyTorch MobileNetV3 (16-D Vector)
          </span>
        </div>

        <div className="bg-slate-850 border border-slate-700/60 rounded-xl p-6 shadow-lg">
          <div className="w-10 h-10 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center mb-4">
            <Activity className="w-5 h-5" />
          </div>
          <h3 className="text-base font-bold text-white mb-1">Modality 2: Skin Image</h3>
          <p className="text-xs text-slate-400 leading-relaxed mb-4">
            Provides complementary dermatological visual information (erythema, vascular dilation, inflammatory signs).
          </p>
          <span className="text-[10px] font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded border border-emerald-500/20 block w-max">
            Complementary Visual Feature
          </span>
        </div>

        <div className="bg-slate-850 border border-slate-700/60 rounded-xl p-6 shadow-lg">
          <div className="w-10 h-10 rounded-lg bg-purple-500/10 text-purple-400 flex items-center justify-center mb-4">
            <Layers className="w-5 h-5" />
          </div>
          <h3 className="text-base font-bold text-white mb-1">Modality 3: Clinical & Lifestyle</h3>
          <p className="text-xs text-slate-400 leading-relaxed mb-4">
            Processes 15 clinical parameters including pain, reflux, constipation, fiber intake, sleep, and stress levels.
          </p>
          <span className="text-[10px] font-mono text-purple-400 bg-purple-500/10 px-2.5 py-1 rounded border border-purple-500/20 block w-max">
            Random Forest & OneHot Pipeline
          </span>
        </div>
      </div>
    </div>
  );
}
