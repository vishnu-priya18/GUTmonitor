import React from 'react';

export default function ModelMetricsCard({ title, modality, metrics, cmPlotUrl, featurePlotUrl }) {
  if (!metrics || metrics.status === 'pending') {
    return (
      <div className="bg-slate-850 border border-slate-700/60 rounded-xl p-6 shadow-md">
        <h4 className="text-sm font-bold text-white mb-2">{title}</h4>
        <div className="text-xs text-amber-400 font-mono bg-amber-950/40 p-3 rounded border border-amber-500/30">
          Model training pending or metrics not yet generated. Run training script.
        </div>
      </div>
    );
  }

  return (
    <div className="bg-slate-850 border border-slate-700/60 rounded-xl p-6 shadow-md space-y-4">
      <div className="flex justify-between items-start border-b border-slate-700/50 pb-3">
        <div>
          <h4 className="text-sm font-bold text-white">{title}</h4>
          <p className="text-[11px] text-slate-400 mt-0.5">{metrics.dataset}</p>
        </div>
        <span className="text-[10px] font-mono bg-teal-500/10 text-teal-300 border border-teal-500/30 px-2 py-0.5 rounded">
          {metrics.num_test_samples} Test Samples
        </span>
      </div>

      {/* Metrics Grid */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
        <div className="bg-slate-900 p-3 rounded-lg border border-slate-800">
          <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Accuracy</span>
          <span className="text-lg font-bold text-teal-400 font-mono">{(metrics.accuracy * 100).toFixed(1)}%</span>
        </div>
        <div className="bg-slate-900 p-3 rounded-lg border border-slate-800">
          <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Macro F1</span>
          <span className="text-lg font-bold text-emerald-400 font-mono">{metrics.f1_macro.toFixed(4)}</span>
        </div>
        <div className="bg-slate-900 p-3 rounded-lg border border-slate-800">
          <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Precision</span>
          <span className="text-lg font-bold text-sky-400 font-mono">{metrics.precision_macro.toFixed(4)}</span>
        </div>
        <div className="bg-slate-900 p-3 rounded-lg border border-slate-800">
          <span className="text-[10px] text-slate-400 uppercase tracking-wider block">Recall</span>
          <span className="text-lg font-bold text-purple-400 font-mono">{metrics.recall_macro.toFixed(4)}</span>
        </div>
      </div>

      {/* Confusion Matrix / Plots */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
        {cmPlotUrl && (
          <div>
            <span className="text-[11px] font-semibold text-slate-300 mb-2 block">Confusion Matrix Heatmap</span>
            <div className="rounded-lg overflow-hidden border border-slate-700 bg-slate-900">
              <img src={cmPlotUrl} alt="Confusion Matrix" className="w-full h-auto object-contain" />
            </div>
          </div>
        )}
        {featurePlotUrl && (
          <div>
            <span className="text-[11px] font-semibold text-slate-300 mb-2 block">Feature Importance Distribution</span>
            <div className="rounded-lg overflow-hidden border border-slate-700 bg-slate-900">
              <img src={featurePlotUrl} alt="Feature Importance" className="w-full h-auto object-contain" />
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
