import React from 'react';
import { History as HistoryIcon, Clock } from 'lucide-react';

export default function History() {
  return (
    <div className="space-y-6">
      <div className="border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <HistoryIcon className="w-5 h-5 text-teal-400" />
          <span>Screening Session History</span>
        </h2>
        <p className="text-xs text-slate-400 mt-0.5">Local session history and previous screening logs</p>
      </div>

      <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4">
        <div className="flex items-center space-x-3 text-xs text-slate-400">
          <Clock className="w-4 h-4 text-teal-400" />
          <span>Showing recent Expo Demo session runs</span>
        </div>

        <div className="space-y-3 text-xs">
          <div className="bg-slate-900 p-4 rounded-lg border border-slate-800 flex justify-between items-center">
            <div>
              <span className="font-bold text-white block">Case A: Healthy Baseline Profile</span>
              <span className="text-[11px] text-slate-400 font-mono">Timestamp: 2026-09-23 • Demo Mode</span>
            </div>
            <span className="bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 px-2.5 py-1 rounded font-bold font-mono">
              Low GI Risk
            </span>
          </div>

          <div className="bg-slate-900 p-4 rounded-lg border border-slate-800 flex justify-between items-center">
            <div>
              <span className="font-bold text-white block">Case B: Moderate GERD/Gastritis Signs</span>
              <span className="text-[11px] text-slate-400 font-mono">Timestamp: 2026-09-23 • Demo Mode</span>
            </div>
            <span className="bg-amber-500/10 text-amber-400 border border-amber-500/30 px-2.5 py-1 rounded font-bold font-mono">
              Moderate GI Risk
            </span>
          </div>

          <div className="bg-slate-900 p-4 rounded-lg border border-slate-800 flex justify-between items-center">
            <div>
              <span className="font-bold text-white block">Case C: Suspected IBS/IBD Profile</span>
              <span className="text-[11px] text-slate-400 font-mono">Timestamp: 2026-09-23 • Demo Mode</span>
            </div>
            <span className="bg-rose-500/10 text-rose-400 border border-rose-500/30 px-2.5 py-1 rounded font-bold font-mono">
              Higher GI Risk
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
