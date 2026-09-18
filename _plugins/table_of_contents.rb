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

  def merge_case_insensitive_tags(tags)
    merged = {}

    tags.each do |name, posts|
      normalized_name = name.to_s.downcase
      merged[normalized_name] ||= { name: name, posts: [] }

      posts.each do |post|
        unless merged[normalized_name][:posts].any? { |existing| existing.url == post.url }
          merged[normalized_name][:posts] << post
        end
      end
    end

    merged.values.sort_by { |entry| entry[:name].to_s.downcase }.map do |entry|
      [entry[:name], entry[:posts]]
    end
  end
end

Liquid::Template.register_filter(TableOfContents)