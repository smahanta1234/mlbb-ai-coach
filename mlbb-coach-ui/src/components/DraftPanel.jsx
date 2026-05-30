export default function DraftPanel({ score = 78, verdict = "Strong Draft" }) {
  return (
    <div className="bg-slate-900 rounded-xl p-5">
      <h2 className="text-xl font-bold mb-4">Draft Intelligence</h2>

      <div className="text-5xl font-bold text-cyan-400">{score}</div>

      <p className="mt-3 text-slate-300">{verdict}</p>
    </div>
  );
}
