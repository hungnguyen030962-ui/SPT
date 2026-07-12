import React, { useMemo } from 'react';
import katex from 'katex';

export function MathRenderer({ text = '', className = '' }) {
  const renderedContent = useMemo(() => {
    if (!text) return '';

    // Regex to match \( inline math \) and \[ display math \]
    const regex = /(\\\(.*?[^\\]\\\)|\\\[.*?[^\\]\\\])/g;
    const parts = text.split(regex);

    return parts.map((part, index) => {
      if (part.startsWith('\\(') && part.endsWith('\\)')) {
        const formula = part.slice(2, -2);
        try {
          const html = katex.renderToString(formula, {
            displayMode: false,
            throwOnError: false,
          });
          return <span key={index} dangerouslySetInnerHTML={{ __html: html }} className="inline-block" />;
        } catch (err) {
          console.error("Katex error:", err);
          return <span key={index}>{part}</span>;
        }
      } else if (part.startsWith('\\[') && part.endsWith('\\]')) {
        const formula = part.slice(2, -2);
        try {
          const html = katex.renderToString(formula, {
            displayMode: true,
            throwOnError: false,
          });
          return <div key={index} dangerouslySetInnerHTML={{ __html: html }} className="my-2 overflow-x-auto" />;
        } catch (err) {
          console.error("Katex error:", err);
          return <div key={index}>{part}</div>;
        }
      }
      // Normal text
      return <span key={index}>{part}</span>;
    });
  }, [text]);

  return <div className={`prose dark:prose-invert max-w-none ${className}`}>{renderedContent}</div>;
}

export default MathRenderer;
