import React, { useState, useEffect } from 'react';
import { BarChart3, RefreshCw } from 'lucide-react';
import ModelMetricsCard from '../components/ModelMetricsCard';
import { api } from '../api/client';

export default function ModelPerformance() {
  const [metricsData, setMetricsData] = useState({
    tongue: null,
    skin: null,
    clinical: null,
    fusion: null
  });
  const [loading, setLoading] = useState(true);

  const fetchAllMetrics = async () => {
    setLoading(true);
    try {
      const [t, s, c, f] = await Promise.all([
        api.getModalityMetrics('tongue'),
        api.getModalityMetrics('skin'),
        api.getModalityMetrics('clinical'),
        api.getModalityMetrics('fusion')
      ]);
      setMetricsData({ tongue: t, skin: s, clinical: c, fusion: f });
    } catch (err) {
      console.error("Error loading metrics:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchAllMetrics();
  }, []);

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center border-b border-slate-800 pb-4">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center gap-2">
            <BarChart3 className="w-5 h-5 text-teal-400" />
            <span>Trained Model Evaluation Metrics</span>
          </h2>
          <p className="text-xs text-slate-400 mt-0.5">Empirical evaluation metrics and confusion matrices generated from offline dataset test splits</p>
        </div>

        <button
          onClick={fetchAllMetrics}
          className="p-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg text-xs font-semibold flex items-center space-x-1.5"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
          <span>Refresh Results</span>
        </button>
      </div>

      <div className="space-y-6">
        <ModelMetricsCard
          title="Modality 1: Tongue Image Classification Model (MobileNetV3 PyTorch)"
          modality="tongue"
          metrics={metricsData.tongue}
          cmPlotUrl="/api/results/tongue/plot/cm"
        />

        <ModelMetricsCard
          title="Modality 2: Skin Image Feature Extractor Model (MobileNetV3 PyTorch)"
          modality="skin"
          metrics={metricsData.skin}
          cmPlotUrl="/api/results/skin/plot/cm"
        />

        <ModelMetricsCard
          title="Modality 3: Clinical & Lifestyle Tabular Model (Random Forest Scikit-Learn)"
          modality="clinical"
          metrics={metricsData.clinical}
          cmPlotUrl="/api/results/clinical/plot/cm"
          featurePlotUrl="/api/results/clinical/plot/feature_imp"
        />

        <ModelMetricsCard
          title="Multimodal Prototype Fusion Model (Gated MLP PyTorch)"
          modality="fusion"
          metrics={metricsData.fusion}
          cmPlotUrl="/api/results/fusion/plot/cm"
        />
      </div>
    </div>
  );
}
