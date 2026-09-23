import React from 'react';
import { Database, FileCode, CheckCircle2 } from 'lucide-react';

export default function DatasetsPage() {
  return (
    <div className="space-y-6">
      <div className="border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <Database className="w-5 h-5 text-teal-400" />
          <span>Datasets & Documentation</span>
        </h2>
        <p className="text-xs text-slate-400 mt-0.5">Authoritative dataset statistics, licensing, and documentation information files</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        
        {/* Tongue Dataset Card */}
        <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-teal-400 uppercase tracking-wider">Tongue Dataset</span>
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
          </div>
          <h3 className="text-sm font-bold text-white">TMC / TCM Tongue Diagnosis Dataset</h3>
          <ul className="text-xs text-slate-300 space-y-1.5 font-mono">
            <li>• Samples: 1,200 Images</li>
            <li>• Resolution: 224x224 RGB</li>
            <li>• Classes: pale, light_red, red, deep_red, purple</li>
            <li>• License: CC-BY 4.0</li>
            <li>• Doc File: <code className="text-teal-300">docs/dataset_info/tongue_dataset.md</code></li>
          </ul>
        </div>

        {/* Skin Dataset Card */}
        <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-emerald-400 uppercase tracking-wider">Skin Dataset</span>
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
          </div>
          <h3 className="text-sm font-bold text-white">ISIC Dermatology Public Dataset</h3>
          <ul className="text-xs text-slate-300 space-y-1.5 font-mono">
            <li>• Samples: 1,500 Images</li>
            <li>• Resolution: 224x224 RGB</li>
            <li>• Classes: benign, erythema, keratosis, vascular, melanocytic</li>
            <li>• Role: Complementary Visual Feature</li>
            <li>• Doc File: <code className="text-emerald-300">docs/dataset_info/skin_dataset.md</code></li>
          </ul>
        </div>

        {/* Clinical Dataset Card */}
        <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-3">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold text-purple-400 uppercase tracking-wider">Clinical Tabular Dataset</span>
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
          </div>
          <h3 className="text-sm font-bold text-white">GI Symptoms & Lifestyle Dataset</h3>
          <ul className="text-xs text-slate-300 space-y-1.5 font-mono">
            <li>• Samples: 1,000 Patient Records</li>
            <li>• Features: 15 Tabular Variables</li>
            <li>• Targets: 3 Risk Categories (Low/Mod/High)</li>
            <li>• Format: CSV Tabular Dataset</li>
            <li>• Doc File: <code className="text-purple-300">docs/dataset_info/clinical_dataset.md</code></li>
          </ul>
        </div>
      </div>
    </div>
  );
}
