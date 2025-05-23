import { formatRef } from "@karrio/lib";
import React from "react";

const EXCLUDE_OPTIONS = ["doc_files", "doc_references"];

interface OptionsDescriptionComponent {
  options: any;
}

export const OptionsDescription = ({
  options,
}: OptionsDescriptionComponent): JSX.Element => {
  return (
    <>
      {Object.entries(options)
        .filter(([key, _]: any) => !EXCLUDE_OPTIONS.includes(key))
        .map(([key, value]: any, index) => (
          <React.Fragment key={index + "item-info"}>
            <p className="is-subtitle is-size-7 my-1 has-text-weight-semibold has-text-grey">
              <span>
                {formatRef(key).toLowerCase()}: <strong>{String(value)}</strong>
                {["insurance", "cash_on_delivery", "declared_value"].includes(
                  key,
                ) && ` ${options.currency || ""}`}
              </span>
            </p>
          </React.Fragment>
        ))}
    </>
  );
};
