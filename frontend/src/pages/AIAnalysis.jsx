import React from 'react';
import { Cpu, Layers, ArrowRight } from 'lucide-react';
import PipelineVisualizer from '../components/PipelineVisualizer';

export default function AIAnalysis({ result }) {
  if (!result) {
    return (
      <div className="bg-slate-850 p-8 rounded-xl border border-slate-700/60 text-center space-y-4">
        <Cpu className="w-12 h-12 text-slate-500 mx-auto" />
        <h3 className="text-base font-bold text-white">No Active Screening Session</h3>
        <p className="text-xs text-slate-400 max-w-md mx-auto">
          Please launch a new screening session from the "New Screening" tab or select an Expo demo profile to view the AI analysis pipeline.
        </p>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      <PipelineVisualizer
        tongueResult={result.tongue}
        skinResult={result.skin}
        clinicalResult={result.clinical}
        fusionResult={result.fusion}
      />

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-3">
          <h4 className="text-xs font-bold text-teal-400 uppercase tracking-wider">Feature Embedding Vectors</h4>
          <div className="text-xs font-mono bg-slate-900 p-3 rounded text-slate-300 space-y-2 overflow-x-auto">
            <div><span className="text-teal-400 font-bold">Tongue Vector (16-D):</span> [{result.tongue?.embedding?.slice(0, 6).map(v=>v.toFixed(3)).join(', ')}, ...]</div>
            <div><span className="text-emerald-400 font-bold">Skin Vector (16-D):</span> [{result.skin?.embedding?.slice(0, 6).map(v=>v.toFixed(3)).join(', ')}, ...]</div>
            <div><span className="text-purple-400 font-bold">Clinical Vector (16-D):</span> [{result.clinical?.embedding?.slice(0, 6).map(v=>v.toFixed(3)).join(', ')}, ...]</div>
          </div>
        </div>

        <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-3">
          <h4 className="text-xs font-bold text-teal-400 uppercase tracking-wider">Gated Multimodal Fusion Weights</h4>
          <p className="text-xs text-slate-300 leading-relaxed">
            The Gated Fusion Layer evaluates modality reliability dynamically, assigning non-linear attention weights to balance visual mucosal cues with self-reported GI risk factors.
          </p>
        </div>
      </div>
    </div>
  );
}
