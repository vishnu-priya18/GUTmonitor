import React, { useRef, useState } from 'react';
import { Upload, Camera, X, Check, RefreshCw } from 'lucide-react';

export default function ImageUploader({ label, sublabel, onImageSelected, currentPreview }) {
  const fileInputRef = useRef(null);
  const [dragActive, setDragActive] = useState(false);

  const handleFile = (file) => {
    if (file && file.type.startsWith('image/')) {
      onImageSelected(file);
    }
  };

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
    if (e.type === 'dragenter' || e.type === 'dragover') {
      setDragActive(true);
    } else if (e.type === 'dragleave') {
      setDragActive(false);
    }
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDragActive(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFile(e.dataTransfer.files[0]);
    }
  };

  return (
    <div className="space-y-2">
      <div className="flex justify-between items-center">
        <label className="text-xs font-semibold text-slate-200">{label}</label>
        {sublabel && <span className="text-[10px] text-slate-400 font-mono">{sublabel}</span>}
      </div>

      {currentPreview ? (
        <div className="relative group rounded-xl overflow-hidden border border-teal-500/40 bg-slate-950 aspect-video flex items-center justify-center">
          <img 
            src={currentPreview} 
            alt="Preview" 
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-slate-950/70 opacity-0 group-hover:opacity-100 transition-all flex items-center justify-center space-x-3">
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              className="p-2 bg-slate-800 hover:bg-slate-700 text-white rounded-lg text-xs font-medium flex items-center gap-1 shadow"
            >
              <RefreshCw className="w-3.5 h-3.5" />
              <span>Replace</span>
            </button>
            <button
              type="button"
              onClick={() => onImageSelected(null)}
              className="p-2 bg-rose-900/80 hover:bg-rose-800 text-rose-200 rounded-lg text-xs font-medium flex items-center gap-1 shadow"
            >
              <X className="w-3.5 h-3.5" />
              <span>Remove</span>
            </button>
          </div>
        </div>
      ) : (
        <div
          onDragEnter={handleDrag}
          onDragLeave={handleDrag}
          onDragOver={handleDrag}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
          className={`border-2 border-dashed rounded-xl p-6 text-center cursor-pointer transition-all ${
            dragActive 
              ? 'border-teal-400 bg-teal-500/10' 
              : 'border-slate-700 hover:border-slate-500 bg-slate-850/50 hover:bg-slate-850'
          }`}
        >
          <div className="w-10 h-10 rounded-full bg-slate-800 flex items-center justify-center mx-auto mb-3 text-teal-400">
            <Upload className="w-5 h-5" />
          </div>
          <p className="text-xs font-medium text-slate-200">
            Click to upload or drag & drop image
          </p>
          <p className="text-[11px] text-slate-400 mt-1">
            Supports PNG, JPG, JPEG up to 10MB
          </p>
        </div>
      )}

      <input 
        ref={fileInputRef}
        type="file" 
        accept="image/*" 
        className="hidden"
        onChange={(e) => e.target.files?.[0] && handleFile(e.target.files[0])}
      />
    </div>
  );
}
