local inspect = require "inspect"

local function auto_join(...)
    local s = ""
    local t = {...}
    local n = select('#', ...)
    for i = 1, n do
        local v = t[i]
        if type(v) == "table" then
            s = s .. inspect(v, {kfilter = {"class", "<metatable>"}}) .. ",\n"
        else
            s = s .. tostring(v) .. "\n"
        end
    end
    return s
end


local tab1 = {33, 44}
local tab = {1, 2, ["tab"] = "tab", ["1"] = 11, {1, 2, 3, tab1}}

print(inspect(tab))


