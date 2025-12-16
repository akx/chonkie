"""Module containing CodeChunker configuration types."""

from dataclasses import dataclass


@dataclass
class MergeRule:
  """Configuration for merging adjacent nodes of specific types."""

  name: str
  node_types: list[str]
  text_pattern: str | None = None
  bidirectional: bool = False

@dataclass
class SplitRule:
  """Configuration for splitting large nodes into smaller chunks.
  
  Args:
    name: Descriptive name for the rule
    node_type: The AST node type to apply this rule to
    body_child: Path to the body node to split. Can be:
      - str: Direct child name (e.g., "class_body")
      - list[str]: Path through nested children (e.g., ["class_declaration", "class_body"])
    exclude_nodes: Optional list of node types to exclude from splitting (e.g., structural punctuation)
    recursive: If True, recursively apply splitting to child nodes of body_child type that exceed chunk_size

  """

  name: str
  node_type: str
  body_child: str | list[str]
  exclude_nodes: list[str] | None = None
  recursive: bool = False

@dataclass
class LanguageConfig:
  """Configuration for a specific programming language's chunking rules."""

  language: str
  merge_rules: list[MergeRule]
  split_rules: list[SplitRule]
