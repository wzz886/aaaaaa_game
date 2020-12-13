-- 模块：
-- 	Core:
-- cc.FileUtils:getInstance():isFileExist(resPath..".lua")  -- 判断文件是否存在

    -- -- 打印文件名
    -- require("util.UIUtil")
    -- require("modules.common.PreResManager")

    -- local view = UIUtil.csLoad("csb/bag/BagView")
    -- local str1, str2 = UIUtil.printChildName(view, 2)
    -- str2 = string.gsub(str2, "%s", "")
    -- str2 = string.gsub(str2, "\"", "")
    -- local tab = StringUtil.stringSplit(str2, ",")
    -- table.sort(tab, function(a, b) return a < b end)

    -- local str = "\nfunction viewName:getViewNameList() \n\treturn {\n\t\t"
    -- for k, v in ipairs(tab) do
    --     if v ~= "" then
    --         if k == #tab then
    --             str = str .. "\"" .. v .. "\"" .. ",\n\t"
    --         else
    --             str = str .. "\"" .. v .. "\"" .. ",\n\t\t"
    --         end
    --     end
    -- end
    -- str = str .. "}\nend"
    -- LogUtil.info("-----控件名----start----\n" .. str .. "\n\n-----控件名----end------")

-- 排序打印getViewNameList
-- function UIUtil.printViewNameList(view)
--     local _, str = UIUtil.printChildName(view)
--     str = string.gsub(str, "%s", "")
--     str = string.gsub(str, "\"", "")
--     local tab = string.split(str, ",")
--     table.sort(tab, function(a, b) return a < b end)

--     local name_str = "\n\n-- 控制名\nfunction aaaaaaa:getViewNameList()\n\treturn\n\t{"
--     local last_sub_str = ""
--     local one_line_num = 5
--     local sub_str = ""
--     local num = 0
--     for _, v in ipairs(tab) do
--         if v ~= "" then
--             num = num + 1
--             sub_str = string.sub(v, 1, 2)
--             if last_sub_str ~= sub_str then
--                 num = 0
--                 last_sub_str = sub_str
--                 name_str = name_str .."\n\t\t\"" ..  v .. "\","
--             else
--                 if num >= one_line_num then
--                     num = 0
--                     name_str = name_str .."\n\t\t\"" ..  v .. "\","
--                 else
--                     name_str = name_str .."\"" ..  v .. "\","
--                 end
--             end
--         end
--     end
--     name_str = name_str .. "\n\t}\nend\n"

--     LogUtil.info(name_str)
-- end 



