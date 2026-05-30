export default function VoicePlayer() {
  return (
    <div className="bg-slate-900 rounded-xl p-5">
      <h2 className="text-xl font-bold mb-4">Voice Analysis</h2>

      <audio controls className="w-full">
        <source src="" type="audio/mp3" />
      </audio>
    </div>
  );
}
