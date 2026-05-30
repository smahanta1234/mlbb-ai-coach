import { useState } from "react";

import DraftPanel from "../components/DraftPanel";
import CoachReport from "../components/CoachReport";
import VoicePlayer from "../components/VoicePlayer";

import { generateGuide } from "../services/api";

export default function Dashboard() {
  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleGenerate() {
    setLoading(true);

    try {
      const result = await generateGuide({
        hero: "Fanny",
        lane: "Jungle",
        playstyle: ["Burst"],

        guide_type: "Rank Push Guide",
        difficulty: "Advanced",

        ally_team: ["Angela", "Tigreal"],
        enemy_team: ["Hayabusa", "Valir"],

        transcript:
          "Fanny invaded enemy jungle at 2 minutes and rotated top lane.",
      });

      setReport(result.guide);
    } catch (error) {
      console.log(error);

      setReport("Could not connect to backend.");
    }

    setLoading(false);
  }

  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      <h1 className="text-4xl font-bold text-cyan-400">🎮 MLBB AI Coach</h1>

      <button
        onClick={handleGenerate}
        className="bg-cyan-500 px-5 py-2 rounded-xl mt-6"
      >
        {loading ? "Analyzing..." : "Generate Analysis"}
      </button>

      <div className="grid grid-cols-3 gap-4 mt-8">
        <DraftPanel />

        <CoachReport report={report} />

        <VoicePlayer />
      </div>
    </div>
  );
}
