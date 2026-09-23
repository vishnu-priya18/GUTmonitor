import React from 'react';
import { AlertTriangle } from 'lucide-react';

export default function DisclaimerBanner() {
  return (
    <div className="bg-amber-950/60 border-l-4 border-amber-500 text-amber-200 p-4 rounded-r-lg mb-6 shadow-md flex items-start space-x-3">
      <AlertTriangle className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
      <div className="text-xs sm:text-sm">
        <span className="font-bold text-amber-300">MEDICAL RESEARCH & SAFETY DISCLAIMER: </span>
        GI-Vision AI is an experimental research prototype for preliminary screening support. It does NOT diagnose gastrointestinal disease and must NOT replace professional medical evaluation or clinical diagnosis.
      </div>
    </div>
  );
}
