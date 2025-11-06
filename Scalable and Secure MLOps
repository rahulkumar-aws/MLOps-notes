# 1 — Databricks = Security + Scale Platform, not “Notebook Engine”
- governance first (UC, identity, lineage)
- scale is not cluster size — scale is *controlled blast radius*

# 2 — Security boundary model
- control-plane isolated
- data-plane per workspace boundary
- private link = required default

# 3 — Identity patterns
- no PAT for automation
- CI/CD = service principal only
- workspace-role ≠ data-role

# 4 — UC is not catalog, UC is policy engine
- grant path = object tree: catalog → schema → table/model
- all ML assets inherit governance

# 5 — Model registry access control
- only pipeline SP can register
- no UI-based promotion

# 6 — Cluster policy = runtime firewall
- enforce driver on on-demand
- workers spot bounded %
- fixed node-types

# 7 — data cost scaling principle
- scale concurrency, not node-size
- cluster size is LAST lever

# 8 — delta protocol = performance backbone
- column-mapping name-mode mandatory
- table constraints enforce contracts

# 9 — zero trust on model endpoints
- endpoint is executable code
- must pin version ID
- NEVER “get latest”

# 10 — immutable truth windows
- delta retention high enough to reconstruct predictions
- rollback > throughput

# 11 — training vs serving cluster class separation
- training = disposable auto kill
- serving = serverless or stable pool

# 12 — DLT incremental feature pipeline
- push updates not full recompute
- 90% cost drop vs batch rebuild

# 13 — serving concurrency > node count
- parallelism scaling wins before hardware scaling

# 14 — spot strategy
- spot usable for ETL/training
- avoid spot on serving

# 15 — GPU scaling principles
- hybrid GPU use when ETL wins < 1.4x CPU
- GPU only when model literally needs tensor

# 16 — network trust zoning
- raw zone (bronze) not allowed for model direct read
- only gold → model

# 17 — policy enforced cookbooks
- DAB deploy pipeline = policy validator stage

# 18 — data contracts enforce correctness
- schema failure kills pipeline
- no silent coercion

# 19 — drift vs poisoning monitoring
- drift = shift
- poisoning = low entropy injection
- both logged as histograms

# 20 — endpoint traffic policies
- canary always
- never jump 0 → 100

# 21 — cold start kill
- serverless auto warm pool
- warm up jobs maintain endpoint readiness

# 22 — SLO tiering
- tier0 (interactive) < 50ms
- tier1 (app scoring) < 200ms
- tier2 (batch) < 1s

# 23 — FinOps tagging per model, not workspace
- env=model_name=model_version
- cost visibility per asset

# 24 — job concurrency limits
- 5 parallel = better scale than 1 giant cluster

# 25 — small files mitigation
- compaction cadence required
- optimize + zorder on feature keys

# 26 — cross region story
- active/passive usually best
- snapshot features, not rebuild

# 27 — lineage is safety net
- pipeline ID + data version + model version must join

# 28 — rollback protocol
- revert endpoint → N-1
- freeze new publish
- root cause via lineage tree

# 29 — security review schedule
- daily: endpoint latency anomaly
- weekly: failed drift thresholds
- monthly: registry audit

# 30 — single final rule
**scale is meaningless if you cannot trace every prediction**  
security = **traceability**
