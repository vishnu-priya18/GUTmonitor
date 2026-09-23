import React from 'react';
import { Activity, Database, BarChart3, Info, BookOpen, Layers, ShieldCheck } from 'lucide-react';

export default function Navbar({ activePage, setActivePage }) {
  const navItems = [
    { id: 'home', label: 'Home', icon: Activity },
    { id: 'new_screening', label: 'New Screening', icon: Layers },
    { id: 'tongue', label: 'Tongue Analysis', icon: Activity },
    { id: 'skin', label: 'Skin Analysis', icon: Activity },
    { id: 'symptoms', label: 'Symptoms & Lifestyle', icon: BookOpen },
    { id: 'results', label: 'Results', icon: ShieldCheck },
    { id: 'performance', label: 'Model Performance', icon: BarChart3 },
    { id: 'datasets', label: 'Datasets', icon: Database },
    { id: 'methodology', label: 'Methodology', icon: BookOpen },
    { id: 'about', label: 'About', icon: Info },
  ];

  return (
    <nav className="bg-slate-900 border-b border-slate-800 sticky top-0 z-50 backdrop-blur bg-slate-900/90">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          
          {/* Brand Logo */}
          <div 
            className="flex items-center space-x-3 cursor-pointer"
            onClick={() => setActivePage('home')}
          >
            <div className="w-9 h-9 rounded-lg bg-teal-600 flex items-center justify-center text-white font-bold text-xl shadow-lg shadow-teal-500/20">
              GI
            </div>
            <div>
              <span className="text-lg font-bold text-white tracking-tight">GI-Vision <span className="text-teal-400">AI</span></span>
              <span className="block text-[10px] text-slate-400 uppercase tracking-widest font-mono">Multimodal BME Research Prototype</span>
            </div>
          </div>

          {/* Nav Items */}
          <div className="hidden lg:flex items-center space-x-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = activePage === item.id;
              return (
                <button
                  key={item.id}
                  onClick={() => setActivePage(item.id)}
                  className={`px-3 py-1.5 rounded-md text-xs font-medium transition-all flex items-center space-x-1.5 ${
                    isActive 
                      ? 'bg-teal-500/10 text-teal-400 border border-teal-500/30' 
                      : 'text-slate-300 hover:text-white hover:bg-slate-800'
                  }`}
                >
                  <Icon className="w-3.5 h-3.5" />
                  <span>{item.label}</span>
                </button>
              );
            })}
          </div>

          {/* Expo Demo Badge */}
          <button
            onClick={() => setActivePage('new_screening')}
            className="bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-600 hover:to-emerald-700 text-white font-semibold text-xs px-3.5 py-2 rounded-lg shadow-lg shadow-teal-500/20 transition-all flex items-center space-x-2"
          >
            <span>Expo Demo Mode</span>
          </button>
        </div>
      </div>
    </nav>
  );
}
