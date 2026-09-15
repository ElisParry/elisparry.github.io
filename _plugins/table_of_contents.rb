module TableOfContents
  HEADING_PATTERN = /<h([1-6])(?:\s+[^>]*)?\sid="([^"]+)"[^>]*>(.*?)<\/h\1>/m

  def table_of_contents(content)
    headings = content.scan(HEADING_PATTERN)
    return "" if headings.empty?

    items = headings.map do |level, id, title|
      %(<li class="post-toc-level-#{level}"><a href="##{id}">#{title}</a></li>)
    end.join

    %(<nav class="post-toc" aria-label="Contents"><h2>Contents</h2><ul>#{items}</ul></nav>)
  end
end

Liquid::Template.register_filter(TableOfContents)