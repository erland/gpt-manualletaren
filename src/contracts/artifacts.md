# Artefaktkontrakt

## ProductCandidate
`manufacturer`, `product_category`, `model_code`, `variant_or_region`, `evidence_url`, `distinguishing_features`, `confidence_note`.

## ManualCandidate
`title`, `url`, `source_type` (`manufacturer`/`other`), `language`, `supported_models`, `verified_content` (boolean), `retrieved_at` (om möjligt).

## Result
`selected_product`, `manual`, `match_status` (`verified`/`probable`/`undetermined`), `match_evidence`, `next_disambiguation_question` (om tillämpligt).

Enbart en URL utgör inte en verifierad manual-matchning.
