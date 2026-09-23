import React from 'react';
import { ArrowRight, Cpu, Layers, Image as ImageIcon, FileText, CheckCircle2 } from 'lucide-react';

export default function PipelineVisualizer({ tongueResult, skinResult, clinicalResult, fusionResult, activeStep = 4 }) {
  return (
    <div className="bg-slate-850 border border-slate-700/60 rounded-xl p-6 shadow-xl mb-8">
      <div className="flex items-center justify-between mb-6 pb-4 border-b border-slate-700/50">
        <div>
          <h3 className="text-base font-bold text-white flex items-center gap-2">
            <Cpu className="w-5 h-5 text-teal-400" />
            <span>Multimodal Neural Feature Fusion Pipeline</span>
          </h3>
          <p className="text-xs text-slate-400 mt-0.5">End-to-end tri-modal feature extraction & gated MLP fusion architecture</p>
        </div>
        <span className="text-[10px] font-mono bg-teal-500/10 text-teal-300 border border-teal-500/30 px-2.5 py-1 rounded">
          Live Backend Execution
        </span>
      </div>

      {/* 3 Modality Encoders Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        
        {/* Tongue Box */}
        <div className={`p-4 rounded-lg border transition-all ${
          tongueResult ? 'bg-slate-800/90 border-teal-500/50' : 'bg-slate-900/50 border-slate-800'
        }`}>
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center gap-2 text-xs font-semibold text-teal-300">
              <ImageIcon className="w-4 h-4 text-teal-400" />
              <span>Modality 1: Tongue</span>
            </div>
            {tongueResult && <CheckCircle2 className="w-4 h-4 text-emerald-400" />}
          </div>
          <div className="text-xs text-slate-300 font-mono mt-1">
            Class: <span className="text-teal-400 font-bold">{tongueResult?.predicted_class || 'Pending'}</span>
          </div>
          <div className="text-[11px] text-slate-400 mt-2 font-mono bg-slate-950 p-2 rounded border border-slate-800">
            Vector: 16-D Normalized Embedding
          </div>
        </div>

        {/* Skin Box */}
        <div className={`p-4 rounded-lg border transition-all ${
          skinResult ? 'bg-slate-800/90 border-teal-500/50' : 'bg-slate-900/50 border-slate-800'
        }`}>
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center gap-2 text-xs font-semibold text-emerald-300">
              <ImageIcon className="w-4 h-4 text-emerald-400" />
              <span>Modality 2: Skin</span>
            </div>
            {skinResult && <CheckCircle2 className="w-4 h-4 text-emerald-400" />}
          </div>
          <div className="text-xs text-slate-300 font-mono mt-1">
            Class: <span className="text-emerald-400 font-bold">{skinResult?.predicted_class || 'Pending'}</span>
          </div>
          <div className="text-[11px] text-slate-400 mt-2 font-mono bg-slate-950 p-2 rounded border border-slate-800">
            Vector: 16-D Skin Embedding
          </div>
        </div>

        {/* Clinical Box */}
        <div className={`p-4 rounded-lg border transition-all ${
          clinicalResult ? 'bg-slate-800/90 border-teal-500/50' : 'bg-slate-900/50 border-slate-800'
        }`}>
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center gap-2 text-xs font-semibold text-purple-300">
              <FileText className="w-4 h-4 text-purple-400" />
              <span>Modality 3: Clinical</span>
            </div>
            {clinicalResult && <CheckCircle2 className="w-4 h-4 text-emerald-400" />}
          </div>
          <div className="text-xs text-slate-300 font-mono mt-1">
            Risk: <span className="text-purple-400 font-bold">{clinicalResult?.predicted_risk || 'Pending'}</span>
          </div>
          <div className="text-[11px] text-slate-400 mt-2 font-mono bg-slate-950 p-2 rounded border border-slate-800">
            Vector: 16-D Tabular Vector
          </div>
        </div>
      </div>

      {/* Fusion Merging Layer */}
      <div className="bg-slate-900 border border-teal-500/30 p-4 rounded-lg flex flex-col md:flex-row items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-lg bg-teal-500/20 border border-teal-500/40 flex items-center justify-center text-teal-400">
            <Layers className="w-5 h-5" />
          </div>
          <div>
            <div className="text-xs font-bold text-white">Gated Prototype Fusion Layer (48-D Concatenation)</div>
            <div className="text-[11px] text-slate-400 mt-0.5">Combines 16-D Tongue + 16-D Skin + 16-D Clinical embeddings into joint screening head</div>
          </div>
        </div>
        
        <div className="flex items-center gap-2">
          <ArrowRight className="w-4 h-4 text-teal-400 hidden md:block" />
          <div className="text-right">
            <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Screening Indication</span>
            <span className="text-xs font-bold text-teal-300">{fusionResult?.preliminary_risk_indication || 'Low / Moderate / Higher Risk'}</span>
          </div>
        </div>
      </div>
    </div>
  );
}
