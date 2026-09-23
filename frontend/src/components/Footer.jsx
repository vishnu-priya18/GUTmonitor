import React from 'react';

export default function Footer() {
  return (
    <footer className="bg-slate-950 border-t border-slate-800 text-slate-400 py-8 text-xs">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-4">
        <div>
          <p className="font-semibold text-slate-200">GI-Vision AI — BME Project Expo 2026</p>
          <p className="text-slate-500 mt-1">Multimodal AI-Based Gastrointestinal Screening Using Tongue & Skin Images, Symptoms & Lifestyle Data</p>
        </div>
        <div className="text-slate-500 text-right">
          <p>Designed for Research & Educational Demonstration</p>
          <p className="mt-1">PyTorch • FastAPI • React • Tailwind CSS</p>
        </div>
      </div>
    </footer>
  );
}
