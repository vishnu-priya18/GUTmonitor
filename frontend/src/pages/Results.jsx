import React from 'react';
import { ShieldCheck, Info } from 'lucide-react';
import RiskGauge from '../components/RiskGauge';
import DisclaimerBanner from '../components/DisclaimerBanner';

export default function Results({ result }) {
  if (!result) {
    return (
      <div className="bg-slate-850 p-8 rounded-xl border border-slate-700/60 text-center space-y-4">
        <ShieldCheck className="w-12 h-12 text-slate-500 mx-auto" />
        <h3 className="text-base font-bold text-white">No Screening Result Loaded</h3>
        <p className="text-xs text-slate-400 max-w-md mx-auto">
          Run a new screening session from the "New Screening" tab or select an Expo demo case.
        </p>
      </div>
    );
  }

  const fusion = result.fusion || {};

  return (
    <div className="space-y-6">
      <DisclaimerBanner />

      <div className="border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <ShieldCheck className="w-5 h-5 text-teal-400" />
          <span>Preliminary Screening Indication Result</span>
        </h2>
        <p className="text-xs text-slate-400 mt-0.5">Summary derived from Gated Multimodal Prototype Fusion</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-1">
          <RiskGauge
            riskLevel={fusion.preliminary_risk_indication}
            confidence={fusion.confidence}
            probabilities={fusion.risk_probabilities}
          />
        </div>

        <div className="lg:col-span-2 space-y-6">
          <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4">
            <h3 className="text-sm font-bold text-white uppercase tracking-wider">Modality Decomposition</h3>

            <div className="space-y-3 text-xs">
              <div className="bg-slate-900 p-3.5 rounded-lg border border-slate-800 flex justify-between items-center">
                <div>
                  <span className="text-teal-400 font-bold block">Modality 1: Tongue Mucosa</span>
                  <span className="text-slate-300 font-semibold">{result.tongue?.predicted_class}</span>
                </div>
                <span className="text-slate-400 font-mono">Confidence: {(result.tongue?.confidence * 100).toFixed(1)}%</span>
              </div>

              <div className="bg-slate-900 p-3.5 rounded-lg border border-slate-800 flex justify-between items-center">
                <div>
                  <span className="text-emerald-400 font-bold block">Modality 2: Complementary Skin</span>
                  <span className="text-slate-300 font-semibold">{result.skin?.predicted_class}</span>
                </div>
                <span className="text-slate-400 font-mono">Confidence: {(result.skin?.confidence * 100).toFixed(1)}%</span>
              </div>

              <div className="bg-slate-900 p-3.5 rounded-lg border border-slate-800 flex justify-between items-center">
                <div>
                  <span className="text-purple-400 font-bold block">Modality 3: GI Symptoms & Lifestyle</span>
                  <span className="text-slate-300 font-semibold">{result.clinical?.predicted_risk}</span>
                </div>
                <span className="text-slate-400 font-mono">Confidence: {(result.clinical?.confidence * 100).toFixed(1)}%</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 text-xs text-slate-300 space-y-2">
            <h4 className="font-bold text-white flex items-center gap-1.5">
              <Info className="w-4 h-4 text-teal-400" />
              <span>Scientific Note on Prototype Fusion</span>
            </h4>
            <p className="leading-relaxed text-slate-400">
              {fusion.disclaimer || "Modality models are trained on validated independent research datasets. Prototype fusion combines normalized feature representations."}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}
