import React from 'react';
import { BookOpen, Cpu, Layers, ShieldAlert } from 'lucide-react';

export default function Methodology() {
  return (
    <div className="space-y-6 max-w-4xl">
      <div className="border-b border-slate-800 pb-4">
        <h2 className="text-xl font-bold text-white flex items-center gap-2">
          <BookOpen className="w-5 h-5 text-teal-400" />
          <span>Research Methodology & Architecture</span>
        </h2>
        <p className="text-xs text-slate-400 mt-0.5">Technical breakdown of feature extraction, embeddings, and gated prototype fusion</p>
      </div>

      <div className="bg-slate-850 p-6 rounded-xl border border-slate-700/60 space-y-4 text-xs text-slate-300 leading-relaxed">
        <h3 className="text-sm font-bold text-white flex items-center gap-2 text-teal-300">
          <Cpu className="w-4 h-4" />
          <span>1. Modality-Specific Feature Extraction</span>
        </h3>
        <p>
          Each data stream is processed by a dedicated encoder network trained on validated research datasets:
        </p>
        <ul className="list-disc pl-5 space-y-1.5 text-slate-400">
          <li><strong className="text-slate-200">Tongue Encoder:</strong> PyTorch MobileNetV3 Small backbone fine-tuned on tongue color and coating categories. Extracts a normalized 16-D tongue embedding vector.</li>
          <li><strong className="text-slate-200">Skin Encoder:</strong> PyTorch CNN fine-tuned on ISIC dermatological images. Extracts a 16-D skin embedding vector designated as complementary visual information.</li>
          <li><strong className="text-slate-200">Clinical Encoder:</strong> Scikit-Learn Random Forest Pipeline with StandardScaler and OneHotEncoder operating on 15 GI symptoms and lifestyle features to extract a 16-D tabular vector.</li>
        </ul>

        <h3 className="text-sm font-bold text-white flex items-center gap-2 text-teal-300 pt-4 border-t border-slate-800">
          <Layers className="w-4 h-4" />
          <span>2. Gated Multimodal Fusion Architecture</span>
        </h3>
        <p>
          The feature vectors (16-D + 16-D + 16-D) are concatenated into a 48-dimensional joint representation. A Gated Multimodal MLP computes non-linear attention weights to generate a final 3-class GI risk indication score (Low, Moderate, Higher Risk).
        </p>

        <h3 className="text-sm font-bold text-white flex items-center gap-2 text-amber-300 pt-4 border-t border-slate-800">
          <ShieldAlert className="w-4 h-4" />
          <span>3. Dataset Compatibility & Scientific Integrity</span>
        </h3>
        <p>
          Because public datasets for tongue mucosa, dermatological skin lesions, and clinical GI symptoms exist in separate research cohorts, **GI-Vision AI does NOT falsely merge unrelated patients**. The prototype fusion layer operates on normalized feature embeddings. Full clinical deployment requires a paired multimodal patient cohort under IRB ethical approval.
        </p>
      </div>
    </div>
  );
}
