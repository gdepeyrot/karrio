import React from 'react';

interface StatusCodeComponent {
  code: string | number;
}

export const StatusCode= ({ code }): JSX.Element =>  {
  if (`${code}`[0] == '2') {
    return <span className={`tag is-success`}>{code}</span>;
  }
  if (`${code}`[0] == '4') {
    return <span className={`tag is-warning`}>{code}</span>;
  }
  if (`${code}`[0] == '5') {
    return <span className={`tag is-danger`}>{code}</span>;
  }
  else {
    return <span className={`tag is-dark`}>{code}</span>;
  }
};
