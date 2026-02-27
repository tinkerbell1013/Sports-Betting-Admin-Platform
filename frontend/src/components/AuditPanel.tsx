type Audit = {
  id: number;
  field_name: string;
  old_value: string | null;
  new_value: string | null;
  changed_at: string;
};

export function AuditPanel({ audits }: { audits: Audit[] }) {
  return (
    <div>
      <h3>Audit History</h3>
      <ul>
        {audits.map(a => (
          <li key={a.id}>
            <strong>{a.field_name}</strong>: {a.old_value} → {a.new_value}
            <br />
            <small>{new Date(a.changed_at).toLocaleString()}</small>
          </li>
        ))}
      </ul>
    </div>
  );
}
