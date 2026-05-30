export default function HeroCard({ hero, role }) {
  return (
    <div className="bg-slate-900 rounded-xl p-4 border border-slate-700 hover:scale-105 transition">
      <h3 className="text-lg font-bold text-cyan-400">{hero}</h3>

      <p className="text-sm text-slate-300 mt-2">{role}</p>
    </div>
  );
}
