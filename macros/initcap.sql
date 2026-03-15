{% macro initcap(column_name) %}
    (
        SELECT list_aggr(
            list_transform(
                string_split(lower({{ column_name }}), ' '),
                x -> CASE 
                    WHEN x IN ('de', 'do', 'da', 'dos', 'das', 'e') 
                    THEN x 
                    ELSE upper(x[1]) || x[2:] 
                END
            ), 
            'string_agg', ' '
        )
    )
{% endmacro %}