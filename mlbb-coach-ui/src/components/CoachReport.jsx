export default function CoachReport({ report }) {
  return (
    <div className="bg-slate-900 rounded-xl p-5">
      <h2 className="text-xl font-bold mb-4">AI Coaching Report</h2>

      {report ? (
        <div className="whitespace-pre-wrap">{report}</div>
      ) : (
        <p className="text-slate-400">
          Generate analysis to see coaching results
        </p>
      )}
    </div>
  );
}
