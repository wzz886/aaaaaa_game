local str_ids = ""
for i = 0, 5 do
	if i > 0 then
		str_ids = str_ids .. ","
	end
	str_ids = str_ids .. "itemid100"
end
print(str_ids)
