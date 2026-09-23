import React from 'react';

export default function RiskGauge({ riskLevel, confidence, probabilities }) {
  const getRiskStyle = (level) => {
    switch (level) {
      case 'Low GI Risk':
        return {
          bg: 'bg-emerald-950/80 border-emerald-500/40 text-emerald-300',
          badge: 'bg-emerald-500 text-slate-950',
          bar: 'bg-emerald-500',
          title: 'LOW GI SCREENING RISK'
        };
      case 'Moderate GI Risk':
        return {
          bg: 'bg-amber-950/80 border-amber-500/40 text-amber-300',
          badge: 'bg-amber-500 text-slate-950',
          bar: 'bg-amber-500',
          title: 'MODERATE GI SCREENING RISK'
        };
      case 'Higher GI Risk':
      default:
        return {
          bg: 'bg-rose-950/80 border-rose-500/40 text-rose-300',
          badge: 'bg-rose-500 text-white',
          bar: 'bg-rose-500',
          title: 'HIGHER GI SCREENING RISK'
        };
    }
  };

  const style = getRiskStyle(riskLevel);

  return (
    <div className={`p-6 rounded-xl border ${style.bg} shadow-lg transition-all`}>
      <div className="flex items-center justify-between mb-4">
        <span className={`text-xs font-bold px-3 py-1 rounded-full uppercase tracking-wider ${style.badge}`}>
          {style.title}
        </span>
        <span className="text-xs font-mono text-slate-400">
          Model Confidence: {(confidence * 100).toFixed(1)}%
        </span>
      </div>

      <div className="text-2xl font-extrabold tracking-tight mb-2">
        {riskLevel}
      </div>

      <p className="text-xs text-slate-300 mb-6 leading-relaxed">
        Preliminary risk score derived via Gated Multimodal Feature Fusion of tongue mucosal patterns, complementary skin visual signs, and structured clinical symptoms.
      </p>

      {/* Probabilities Breakdown */}
      {probabilities && (
        <div className="space-y-3 pt-4 border-t border-slate-800/80">
          <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block">Class Probability Distribution</span>
          {Object.entries(probabilities).map(([key, val]) => (
            <div key={key} className="space-y-1">
              <div className="flex justify-between text-xs font-mono">
                <span className="text-slate-300">{key}</span>
                <span className="text-slate-400">{(val * 100).toFixed(1)}%</span>
              </div>
              <div className="w-full bg-slate-800 rounded-full h-1.5 overflow-hidden">
                <div 
                  className={`h-1.5 rounded-full transition-all duration-500 ${
                    key === riskLevel ? style.bar : 'bg-slate-600'
                  }`}
                  style={{ width: `${Math.max(2, val * 100)}%` }}
                />
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
